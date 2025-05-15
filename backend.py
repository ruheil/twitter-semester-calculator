from PIL import Image, ImageDraw
from datetime import date


# -- CHANGE THIS BEFORE SEMESTER STARTS --
start_date = date(2025, 2, 2)
end_date = date(2025, 5, 15)
semester_name = "ربيع 25"
# ------------------------------------------


total_days = (end_date - start_date).days

def get_percentage():
    current_date = date.today()
    days_till_finish = (end_date - current_date).days
    percentage = round(abs(100 - (days_till_finish / total_days * 100)), 1)
    return percentage, days_till_finish

def get_caption():
    percentage, days = get_percentage()
    caption = "فصل " + semester_name + " انتهى بمقدار " + str(percentage) + "%.. "

    if days == 0:
        caption += "مبارك!"
    elif days == 1:
        caption += "تبقى يوم واحد!"
    elif days == 2:
        caption += "تبقى يومان"
    elif days <= 10:
        caption += "تبقى " + str(days) + " أيام"
    else:
        caption += "تبقى " + str(days) + " يوماً"

    return caption


def create_progress_bar(width=1116, height=223, bar_color=(0, 255, 0), bg_color=(255, 255, 255)):
    percentage, _ = get_percentage()
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    draw.rectangle([30, 30, width - 30, height - 30], fill=(0, 0, 0))

    draw.rectangle([15, 15, width - 15, height - 15], outline=(0, 0, 0))

    bar_max_width = width - 60
    bar_width = int(bar_max_width * (min(percentage, 100) / 100.0))
    draw.rectangle([30, 30, 30 + bar_width, height - 30], fill=bar_color)

    img.save("progressbar.jpg")

