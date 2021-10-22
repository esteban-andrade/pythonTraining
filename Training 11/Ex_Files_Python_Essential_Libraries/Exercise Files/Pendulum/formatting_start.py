# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# create a datetime and print it
dt1 = pendulum.datetime(2021, 10, 15, 15, 30)
print(dt1)

# TODO: use some formatting functions
print(dt1.to_date_string())
print(dt1.to_time_string())
print(dt1.to_datetime_string())


# TODO: use functions for nice formatting
print("\n")
print(dt1.to_formatted_date_string())
print(dt1.to_day_datetime_string())

# TODO: use some common formats
print("\n")
print(dt1.to_cookie_string())  # print it like a browser cookie string
print(dt1.to_iso8601_string())  # other formats
print(dt1.to_rfc822_string())


# TODO: use the format function for pretty printing
print("\n")
print(dt1.format("YYYY MM-DD HH:MM A"))
print(dt1.format("dddd DD MMMM YYYY"))


# TODO: use localization
print(dt1.format("dddd DD MMMM YYYY", locale="de"))  # german
print(dt1.format("dddd DD MMMM YYYY", locale="fr"))  # french
print(dt1.format("dddd DD MMMM YYYY", locale="es"))  # spanish
