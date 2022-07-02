import instaloader


ig = instaloader.Instaloader()

dp = input('Enter insta username : ')

ig.download_profile(dp, profile_pic_only=True)

