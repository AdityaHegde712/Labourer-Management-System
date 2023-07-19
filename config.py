# Add/Remove worker
first_name = None
last_name = None
full_name = None
phone_no = None
add_remove_worker = None

# Attendance
dates = ['2023-06-15', '2023-06-16', '2023-06-17', '2023-06-18', '2023-06-19', 
         '2023-06-20']
names = ['Rajesh Patel', 'Manjula Devi', 'Harish Singh', 'Geeta Yadav', 'Anil Sharma', 
         'Preeti Verma']
tasks = ['Planting crops', 'Irrigating fields', 'Harvesting produce', 'Feeding livestock', 
         'Maintaining farm equipment', 'Repairing fences']

# Final Cost
daily_total = 1111
monthly_total = 11111
grand_total = 12222

# Get Data
date_range = ['2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11', '2023-06-12', '2023-06-13', 
              '2023-06-14', '2023-06-15', '2023-06-16', '2023-06-17', '2023-06-18', '2023-06-19', 
              '2023-06-20', '2023-06-21', '2023-06-22']
sample_daily_entries = [('2023-05-22', 'Farm Labourer', '+91025070276', 'Farm Work', '$53'), 
                        ('2023-05-23', 'Farm Labourer', '+91504828303', 'Farm Work', '$51'), 
                        ('2023-05-24', 'Farm Labourer', '+91816195340', 'Farm Work', '$66'), 
                        ('2023-05-25', 'Farm Labourer', '+91287387617', 'Farm Work', '$36'), 
                        ('2023-05-26', 'Farm Labourer', '+91168760743', 'Farm Work', '$30'), 
                        ('2023-05-27', 'Farm Labourer', '+91334374991', 'Farm Work', '$42'), 
                        ('2023-05-28', 'Farm Labourer', '+91803620215', 'Farm Work', '$48'), 
                        ('2023-05-29', 'Farm Labourer', '+91146147238', 'Farm Work', '$61'), 
                        ('2023-05-30', 'Farm Labourer', '+91146708163', 'Farm Work', '$39'), 
                        ('2023-05-31', 'Farm Labourer', '+91416462336', 'Farm Work', '$37'), 
                        ('2023-06-01', 'Farm Labourer', '+91409636865', 'Farm Work', '$57'), 
                        ('2023-06-02', 'Farm Labourer', '+91686073927', 'Farm Work', '$53'), 
                        ('2023-06-03', 'Farm Labourer', '+91043488052', 'Farm Work', '$66'), 
                        ('2023-06-04', 'Farm Labourer', '+91917168062', 'Farm Work', '$60'), 
                        ('2023-06-05', 'Farm Labourer', '+91593560496', 'Farm Work', '$52'), 
                        ('2023-06-06', 'Farm Labourer', '+91952001077', 'Farm Work', '$49'), 
                        ('2023-06-07', 'Farm Labourer', '+91743251757', 'Farm Work', '$33'), 
                        ('2023-06-08', 'Farm Labourer', '+91808187685', 'Farm Work', '$69'), 
                        ('2023-06-09', 'Farm Labourer', '+91292599915', 'Farm Work', '$52'), 
                        ('2023-06-10', 'Farm Labourer', '+91630626508', 'Farm Work', '$32'), 
                        ('2023-06-11', 'Farm Labourer', '+91289331375', 'Farm Work', '$67'), 
                        ('2023-06-12', 'Farm Labourer', '+91680463498', 'Farm Work', '$62'), 
                        ('2023-06-13', 'Farm Labourer', '+91499937702', 'Farm Work', '$47'), 
                        ('2023-06-14', 'Farm Labourer', '+91803370997', 'Farm Work', '$39'), 
                        ('2023-06-15', 'Farm Labourer', '+91707096998', 'Farm Work', '$42'), 
                        ('2023-06-16', 'Farm Labourer', '+91591628476', 'Farm Work', '$51'), 
                        ('2023-06-17', 'Farm Labourer', '+91504158022', 'Farm Work', '$70'), 
                        ('2023-06-18', 'Farm Labourer', '+91400727662', 'Farm Work', '$60'), 
                        ('2023-06-19', 'Farm Labourer', '+91103224036', 'Farm Work', '$63'), 
                        ('2023-06-20', 'Farm Labourer', '+91395512746', 'Farm Work', '$31'), 
                        ('2023-06-21', 'Farm Labourer', '+91778387093', 'Farm Work', '$67')]
sample_monthly_entries = [('2023-05-27', 'Sarah Fields', 'Livestock Care', '$42'),
                          ('2023-05-28', 'David Agrarian', 'Crop Spraying', '$53'),
                          ('2023-05-29', 'Michael Gardener', 'Irrigation', '$58'),
                          ('2023-05-30', 'John Farmer', 'Planting', '$37'),
                          ('2023-05-31', 'Emily Harvest', 'Harvesting', '$65'),
                          ('2023-06-01', 'David Agrarian', 'Irrigation', '$58'),
                          ('2023-06-02', 'John Farmer', 'Crop Spraying', '$53'),
                          ('2023-06-03', 'Sarah Fields', 'Harvesting', '$65'),
                          ('2023-06-04', 'Michael Gardener', 'Planting', '$37'),
                          ('2023-06-05', 'Emily Harvest', 'Irrigation', '$58'),
                          ('2023-06-06', 'John Farmer', 'Harvesting', '$65'),
                          ('2023-06-07', 'David Agrarian', 'Livestock Care', '$42'),
                          ('2023-06-08', 'Sarah Fields', 'Irrigation', '$58'),
                          ('2023-06-09', 'Michael Gardener', 'Crop Spraying', '$53'),
                          ('2023-06-10', 'David Agrarian', 'Crop Spraying', '$53'),
                          ('2023-06-11', 'Sarah Fields', 'Irrigation', '$58'),
                          ('2023-06-12', 'Emily Harvest', 'Livestock Care', '$42'),
                          ('2023-06-13', 'David Agrarian', 'Irrigation', '$58'),
                          ('2023-06-14', 'John Farmer', 'Planting', '$37'),
                          ('2023-06-15', 'Michael Gardener', 'Crop Spraying', '$53'),
                          ('2023-06-16', 'Emily Harvest', 'Crop Spraying', '$53'),
                          ('2023-06-17', 'Sarah Fields', 'Irrigation', '$58'),
                          ('2023-06-18', 'David Agrarian', 'Planting', '$37'),
                          ('2023-06-19', 'Michael Gardener', 'Livestock Care', '$42'),
                          ('2023-06-20', 'John Farmer', 'Irrigation', '$58'),
                          ('2023-06-21', 'Emily Harvest', 'Harvesting', '$65'),
                          ('2023-06-22', 'Michael Gardener', 'Harvesting', '$65'),
                          ('2023-06-23', 'John Farmer', 'Crop Spraying', '$53')]

# Worker Details
worker_details = [
    ("John Doe", "+91 9876543210"),
    ("Jane Smith", "+91 8765432109"),
    ("Robert Johnson", "+91 7654321098"),
    ("Emily Brown", "+91 6543210987"),
    ("Michael Davis", "+91 5432109876"),
    ("Sarah Wilson", "+91 4321098765"),
    ("David Taylor", "+91 3210987654"),
    ("Jessica Martinez", "+91 2109876543"),
    ("Daniel Anderson", "+91 1098765432"),
    ("Olivia Thomas", "+91 0987654321")
]
