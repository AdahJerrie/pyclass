import unittest
from campusflow.tickets import (
    calculate_priority,
    create_ticket,
    get_ticket_by_id,
    list_tickets,
)


class TestTickets(unittest.TestCase):
    """Automated unit tests for F1 (Create & Priority) and F2 (List & View)."""

    def test_high_urgency_and_twelve_users_is_critical(self):
        tickets = []
        ticket = create_ticket(tickets, "Campus Wi-Fi is down", "Network", "high", 12)
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    def test_high_urgency_and_two_users_is_high(self):
        tickets = []
        ticket = create_ticket(tickets, "Projector broken", "Hardware", "high", 2)
        self.assertEqual(ticket["priority"], "high")

    def test_low_urgency_and_four_users_is_medium(self):
        tickets = []
        ticket = create_ticket(tickets, "Slow printer", "Hardware", "low", 4)
        self.assertEqual(ticket["priority"], "medium")

    def test_low_urgency_and_one_user_is_low(self):
        tickets = []
        ticket = create_ticket(tickets, "Mouse battery low", "Hardware", "low", 1)
        self.assertEqual(ticket["priority"], "low")

    def test_priority_exact_boundaries(self):
        # 10 users with high urgency -> critical (Rule 1 boundary)
        self.assertEqual(calculate_priority("high", 10), "critical")
        # 10 users with low urgency -> high (Rule 2 boundary)
        self.assertEqual(calculate_priority("low", 10), "high")
        # 3 users with low urgency -> medium (Rule 3 boundary)
        self.assertEqual(calculate_priority("low", 3), "medium")
        # 1 user with medium urgency -> medium (Rule 3 urgency match)
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_zero_affected_users_is_rejected_without_corrupting_list(self):
        tickets = []
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Wi-Fi issue", "Network", "low", 0)
        self.assertEqual(len(tickets), 0)

    def test_invalid_inputs_are_rejected(self):
        tickets = []
        # Blank title
        with self.assertRaises(ValueError):
            create_ticket(tickets, "   ", "Network", "low", 2)
        # Invalid category
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Bad category", "Cafeteria", "low", 2)
        # Invalid urgency
        with self.assertRaises(ValueError):
            create_ticket(tickets, "Bad urgency", "Software", "extreme", 2)
        # Negative, decimal, text, and boolean affected_users
        for bad_users in (-5, 3.5, "3.5", "ten", True):
            with self.assertRaises(ValueError):
                create_ticket(tickets, "Bad users", "Software", "low", bad_users)
        self.assertEqual(len(tickets), 0)

    def test_case_normalization_and_unique_sequential_ids(self):
        tickets = []
        t1 = create_ticket(tickets, "  Router reset  ", "network", "HIGH", "15")
        t2 = create_ticket(tickets, "IDE crash", "SOFTWARE", "Medium", 1)

        self.assertEqual(t1["id"], "T001")
        self.assertEqual(t1["title"], "Router reset")
        self.assertEqual(t1["category"], "Network")
        self.assertEqual(t1["urgency"], "high")
        self.assertEqual(t1["affected_users"], 15)
        self.assertEqual(t2["id"], "T002")
        self.assertEqual(len(list_tickets(tickets)), 2)

    def test_get_ticket_by_id_and_unknown_id_rejected(self):
        tickets = []
        create_ticket(tickets, "VPN error", "Network", "medium", 5)

        found = get_ticket_by_id(tickets, "t001")
        self.assertEqual(found["id"], "T001")

        with self.assertRaises(ValueError):
            get_ticket_by_id(tickets, "T999")


if __name__ == "__main__":
    unittest.main()