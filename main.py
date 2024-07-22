import requests

# urls = [
#     "https://quastech.in", "https://innovaccer.com/contact-us",
#     "https://www.infogain.com/about/contact-us/"
# ]


# Func to split on "
def split_quote(text):
  return text.split('"')


# Remove mailto:
def remove_mailto(email_str):
  return email_str.replace("mailto:", "")


# Function to find email in a list
def find_email(data_list):
  email_list = []
  for el in data_list:
    if "@" in el and "." in el and "/" not in el:
      email_list.append(remove_mailto(el))
  return email_list


# Function to request a URL
def fetch(url):
  res = requests.get(url)

  if res.status_code == 200:
    return res.text

  print(f"Failed with error code {res.status_code}")
  return ""


# Taking Input
urls = []

while True:
  user_input = input("Enter a URL or N to exit: ")
  if user_input == "N":
    print("URL List Ready!")
    break

  if "://" not in user_input:
    print("Enter a valid URL!")
  else:
    urls.append(user_input)

emails = []
for url in urls:
  data = fetch(url)
  data_list = split_quote(data)
  email_list = find_email(data_list)
  emails.extend(email_list)

# To remove duplicates using iteration
# unique_emails = []
# for email in emails:
#   if email not in unique_emails:
#     unique_emails.append(email)

# Remove duplicates
emails = set(emails)

print(emails)

# Write output to a file
f = open('emails.txt', 'w')
f.write(str(emails))
f.close()