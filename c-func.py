t = "thIS Is A tExT"

def caps(text):
    return text.upper()

def low(text):
    return text.lower()

def process(fn, txt_val):
    processed = fn(txt_val)
    return processed

# print(caps(t))
print(process(low, t))
print(process(caps, t))

hi_fn = lambda x: f"Hi, {x}"

print(hi_fn("Ck"), type(hi_fn))

print(process(lambda x: f"Hello, {x}", "TAP"))