boilerplate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""

# for i in range(2, 4):
#     with open(f"task_{i}.html","w") as files:
#         files.write(boilerplate)

# add missed file
with open("task_1.html", "w") as missed_file:
    missed_file.write(boilerplate)