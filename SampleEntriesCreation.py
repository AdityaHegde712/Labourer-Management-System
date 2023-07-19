import worker as w
import tasks
import dailyEntries as de
import attendance

def initialize_database():
    # Enter workers list
    workers = [
        {
            'name': 'John Smith',
            'phone_no': '1234567890'
        },
        {
            'name': 'Emma Johnson',
            'phone_no': '9876543210'
        },
        {
            'name': 'Michael Davis',
            'phone_no': '4567890123'
        },
        {
            'name': 'Sophia Wilson',
            'phone_no': '8901234567'
        },
        {
            'name': 'Daniel Thompson',
            'phone_no': '2345678901'
        },
        {
            'name': 'Olivia Martinez',
            'phone_no': '9012345678'
        },
        {
            'name': 'William Anderson',
            'phone_no': '3456789012'
        },
        {
            'name': 'Ava Taylor',
            'phone_no': '7890123456'
        },
        {
            'name': 'David Hernandez',
            'phone_no': '5678901234'
        },
        {
            'name': 'Mia Moore',
            'phone_no': '0123456789'
        }
    ]
    for entry in workers:
        w.insert_one(entry)


    # Sample Daily Entries
    sample_daily_entries = [
        {
            'name': 'Michael Davis',
            'phone_no': '4567890123',
            'task': 'Cleaning animal pens',
            'wage': 162,
            'date': '2023-06-03'
        },
        {
            'name': 'David Hernandez',
            'phone_no': '5678901234',
            'task': 'Milking cows',
            'wage': 173,
            'date': '2023-06-12'
        },
        {
            'name': 'David Hernandez',
            'phone_no': '5678901234',
            'task': 'Plowing fields',
            'wage': 133,
            'date': '2023-06-19'
        },
        {
            'name': 'Olivia Martinez',
            'phone_no': '9012345678',
            'task': 'Planting seeds',
            'wage': 149,
            'date': '2023-06-06'
        },
        {
            'name': 'Mia Moore',
            'phone_no': '0123456789',
            'task': 'Plowing fields',
            'wage': 70,
            'date': '2023-06-29'
        },
        {
            'name': 'Ava Taylor',
            'phone_no': '7890123456',
            'task': 'Plowing fields',
            'wage': 167,
            'date': '2023-06-15'
        },
        {
            'name': 'Olivia Martinez',
            'phone_no': '9012345678',
            'task': 'Pruning fruit trees',
            'wage': 148,
            'date': '2023-06-07'
        },
        {
            'name': 'Michael Davis',
            'phone_no': '4567890123',
            'task': 'Gathering eggs',
            'wage': 146,
            'date': '2023-06-04'
        },
        {
            'name': 'John Smith',
            'phone_no': '1234567890',
            'task': 'Planting seeds',
            'wage': 51,
            'date': '2023-06-26'
        },
        {
            'name': 'David Hernandez',
            'phone_no': '5678901234',
            'task': 'Pruning fruit trees',
            'wage': 84,
            'date': '2023-06-23'
        },
        {
            'name': 'Michael Davis',
            'phone_no': '4567890123',
            'task': 'Harvesting vegetables',
            'wage': 144,
            'date': '2023-06-30'
        },
        {
            'name': 'Daniel Thompson',
            'phone_no': '2345678901',
            'task': 'Fertilizing fields',
            'wage': 71,
            'date': '2023-06-28'
        },
        {
            'name': 'Ava Taylor',
            'phone_no': '7890123456',
            'task': 'Weeding',
            'wage': 101,
            'date': '2023-06-27'
        },
        {
            'name': 'Ava Taylor',
            'phone_no': '7890123456',
            'task': 'Maintaining farm equipment',
            'wage': 93,
            'date': '2023-06-08'
        },
        {
            'name': 'William Anderson',
            'phone_no': '3456789012',
            'task': 'Repairing fences',
            'wage': 82,
            'date': '2023-06-03'
        }
    ]
    for entry in sample_daily_entries:
        de.insert_one(entry)


    sample_monthly_entries = [
        {'date': '2023-06-01', 'task': 'Planting seeds', 'wage': 212, 'worker_id': 1},
        {'date': '2023-06-02', 'task': 'Plowing fields', 'wage': 100, 'worker_id': 2}, 
        {'date': '2023-06-03', 'task': 'Cleaning animal pens', 'wage': 206, 'worker_id': 1},
        {'date': '2023-06-04', 'task': 'Gathering eggs', 'wage': 257, 'worker_id': 8},
        {'date': '2023-06-05', 'task': 'Cleaning animal pens', 'wage': 117, 'worker_id': 3},
        {'date': '2023-06-06', 'task': 'Planting seeds', 'wage': 261, 'worker_id': 4},
        {'date': '2023-06-07', 'task': 'Pruning fruit trees', 'wage': 259, 'worker_id': 7},
        {'date': '2023-06-08', 'task': 'Gathering eggs', 'wage': 211, 'worker_id': 4},
        {'date': '2023-06-09', 'task': 'Milking cows', 'wage': 65, 'worker_id': 5},
        {'date': '2023-06-10', 'task': 'Pruning fruit trees', 'wage': 238, 'worker_id': 6},
        {'date': '2023-06-11', 'task': 'Planting seeds', 'wage': 215, 'worker_id': 7},
        {'date': '2023-06-12', 'task': 'Milking cows', 'wage': 289, 'worker_id': 2},
        {'date': '2023-06-13', 'task': 'Plowing fields', 'wage': 62, 'worker_id': 8},
        {'date': '2023-06-14', 'task': 'Cleaning animal pens', 'wage': 211, 'worker_id': 9},
        {'date': '2023-06-15', 'task': 'Plowing fields', 'wage': 243, 'worker_id': 6},
        {'date': '2023-06-16', 'task': 'Gathering eggs', 'wage': 52, 'worker_id': 10},
        {'date': '2023-06-19', 'task': 'Plowing fields', 'wage': 227, 'worker_id': 3},
        {'date': '2023-06-23', 'task': 'Pruning fruit trees', 'wage': 134, 'worker_id': 10},
        {'date': '2023-06-26', 'task': 'Planting seeds', 'wage': 101, 'worker_id': 9},
        {'date': '2023-06-29', 'task': 'Plowing fields', 'wage': 149, 'worker_id': 5}
    ]
    for entry in sample_monthly_entries:
        attendance.insert_one(entry)


    # Sample Activity list
    task_list = [
        "Planting seeds",
        "Watering crops",
        "Weeding",
        "Fertilizing fields",
        "Harvesting vegetables",
        "Pruning fruit trees",
        "Milking cows",
        "Feeding livestock",
        "Cleaning animal pens",
        "Repairing fences",
        "Plowing fields",
        "Maintaining farm equipment",
        "Herding sheep",
        "Gathering eggs",
        "Applying pest control"
    ]
    for task in task_list:
        tasks.insert_one(task)