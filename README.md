# Scraper
Scraper script, that takes care of downloading images, video and datasheet from website 
https://www.lights.co.uk/philips-hue-white-color-impress-led-pillar-light.html

# Specific Requirements (For Selenium WebDriver): 
- Mozzila Firefox Browser https://www.mozilla.org/
- Geckodriver https://github.com/mozilla/geckodriver/releases
# Installation:
- create virtual enviroment
- activate virtual enviroment
- extract and put geckodriver.exe in path that was mentioned above Scraper/interview/interview
- make sure that all requirements are satisfied

# Usage:
- open terminal 
- make sure that you are located in Scraper/interview/interview
- type: ```scrapy crawl lights_co_uk```
## After processing there will be a two new folders called: 
- downloaded_files (there should be an video file and datasheet)
- downloaded_images (there should be 9 images from swiper)
