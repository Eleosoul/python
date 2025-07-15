user_data = ['Alex', 23]

def user_info(name, comments_qty):
	if not comments_qty:
		return f"{name} has no commets"

	return f"{name} has {comments_qty} commets"

print(user_info(*user_data))