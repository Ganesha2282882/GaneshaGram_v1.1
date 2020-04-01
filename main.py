print("GaneshaGram")
print("Options:\n")
ops = ["post", "view"]
print(ops)
main = input()

if main == "post":
  title = input("Enter a title for your post:  ")
  body = input("Enter a body for your post:  ")

  f = open("posts.txt", "a")
  f.write(title + "\n")
  f.write(body + "\n")
  f.close()
  print("Thank you for posting!")

if main == "view":
  f = open("posts.txt", "r")
  print(f.read()) 
  print("It looks like you reached the end! :(")