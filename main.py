dz = "12"
work_dz = "1.5"
course = "Python"
dz_int = int(dz)
work_dz_float = float(work_dz)
deadline_dz = work_dz_float / dz_int
print("Курс: ", course ,"всего задач:",dz, "затрачено часов:", work_dz, "среднее время выполнения", deadline_dz)