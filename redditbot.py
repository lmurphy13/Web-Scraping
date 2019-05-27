import praw
import smtplib

def generate_body(filename):
	reddit = praw.Reddit(client_id="zVwkt8YwVkiR2w",
					client_secret="DV-nNaWtLmdX0XdcH4LikB9tBCU",
					user_agent="Meme Scraper")

	new_posts = reddit.subreddit("ProgrammerHumor").new(limit=5)

	with open(filename, "w") as f:
		f.write("Hello PERSON_NAME,\n\n")
		f.write("Here is your hourly output from r/ProgrammerHumor!\n\n")

		num = 1
		for post in new_posts:
			print("{}.\tTitle: {}\n\tAuthor: {}\n\tText: {}\n\tURL: {}\n".format(num, post.title, post.author, post.selftext, post.url))
			f.write("{}.\tTitle: {}\n\tAuthor: {}\n\tText: {}\n\tURL: {}\n".format(num, post.title, post.author, post.selftext, post.url))
			
			if post.num_comments > 0:
				print("\tSome comments...")
				f.write("\tSome comments...")
				com_num = 1
				for comment in post.comments:
					print("\t{}. {}\n".format(com_num, comment.body))
					f.write("\t{}. {}\n".format(com_num, comment.body))
					com_num += 1
			print("\n")
			f.write("\n")
			num += 1

		f.write("Have a super day!\n\n")
		f.write("SENDER")

def get_contacts(filename):
	names = []
	emails = []

	with open(filename, "r") as contacts:
		for contact in contacts:
			names.append(contact.split()[0])
			emails.append(contact.split()[1])
	return names, emails

generate_body("message.txt")		

names, emails = get_contacts("contacts.txt")

# s = smtplib.SMTP(host="smtp.gmail.com", port=587)
# s.starttls()
# s.login("liammurphy513@gmail.com", "deepspace8675309")

print(names)

for name in names:
	with open("message.txt", "r") as f:
		lines = list(f)
		for line in lines:
			if "PERSON_NAME" in line:
				line.replace("PERSON_NAME", name)
			if "SENDER" in line:
				line.replace("SENDER", "Liam")

		for line in lines:
			print(line)


