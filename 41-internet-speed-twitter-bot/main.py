from speed_scrapper import *
from twitter_bot import *

actual_download_speed, actual_upload_speed = get_speeds()
internet_provider_twitter = ''

tweet = f"Hey {internet_provider_twitter}, According to my contract my download/upload speeds should be 900Mbps/800Mbps.\nBut my actual download and upload speeds are {actual_download_speed}Mbps/{actual_upload_speed}Mbps"

send_tweet(tweet)
