from random import choice

# Quotes to interact with Sarah's Bot
def aaron():
	quotes = ["? Aaron, I have a question.",
			"? Dr. Kaloti, may I ask a question?",
			"? Hey Aaron, just a quick question.",
			"? Aaron, can I ask a question?",
			"? Hey Aaron?",
			"? Hey Aaron, can I ask a question about the homework?",
			"? Aaron, could I ask one more quick question?"]
	return choice(quotes)

# Quotes to interact with Matthew's Bot
def homework():
	quotes = ["Hey! No collaboration allowed on asssignments. It's not good to cheat",
			"Y'all gonna get it trouble if you try to search answers on Chegg",
			"What a nerd lol... who even talks about homework and tests anyway...",
			"Remember, no collaboration on assingnments. Only an egghead would do that.",
			"I'm pretty dumb so I just never do homework or tests.",
			"OOOooo y'all be talking about class. That's pretty sus ngl"]
	return choice(quotes)

# Quotes for Mia
def mia():
	quotes = ["Kombuchan is literally like the smartest person I know... I wish I could ascend to that level one day!",
			"Wow... you're actually so smart. I strive to reach your level one day kombuchan.",
			"Kombuchan's brain literally operates on another dimension... so smart...",
			"Ingenius!! Truly the pinnacle of human intellect!"]
	return choice(quotes)

# Quotes for Ian
def ian():
	quotes = ["What is the math wizard doing on the ECS 36A Server. We are all blessed to be in your presence!",
			"I mean I'm not a big fan of onions, but krusty onions are actually pretty nice",
			"Okay, we get that you're smart, but there's really no reason to flex so hard!!"]
	return choice(quotes)

# Quotes for Matthew
def matt():
	quotes = ["Did you know there are 35,186 students at Davis... of which 59% are female",
			"Hello kind sir, your zoom backgrounds are truly iconic!!",
			"Just a quick reminder from Aaron - NO DISTRACTING ZOOM BACKGROUNDS"]
	return choice(quotes)
