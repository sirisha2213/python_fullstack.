# set
# Take number of images
img_count = int(input("Enter number of images: "))

# Image set input
images = set()
for i in range(img_count):
    images.add(input("Enter image name: "))

# Take number of videos
vid_count = int(input("\nEnter number of videos: "))

# Video set input
videos = set()
for i in range(vid_count):
    videos.add(input("Enter video name: "))

# Display available images
print("\nAvailable Images:")
for img in images:
    print(img)

print("\nAvailable videos:")
for vid in videos:
    print(videos)

# User selects an image
selected_image = input("\nSelect an image to display: ")
selected_videos = input('\nSelect an video to display:')

if selected_videos in videos:
    print("video sent :", selected_videos)
else:
    print("video  not found")

 Display result
if selected_image in images:
    print("image sent", selected_image)
else:
    print("Image not found")


