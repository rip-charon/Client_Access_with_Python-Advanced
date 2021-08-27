from PIL import ImageGrab

file = open('screen.png', 'w')

screenshot = ImageGrab.grab(all_screens=True) # Take a screenshot that includes all screens
screenshot.save(file, 'PNG')  # Save the image to the file object as a PNG

file.close()  # Make sure to close the file when you're done

