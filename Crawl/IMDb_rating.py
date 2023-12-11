from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mysql.connector
conn = mysql.connector.connect(host = "localhost", password = "123456", user = "root")

mycursor = conn.cursor()

page_url = "https://www.imdb.com/title/tt6791350/?ref_=adv_li_tt"
driver = webdriver.Chrome()
driver.get(page_url)

# driver.execute_script("window.scrollTo(0, 5000);")

# driver.execute_script("window.scrollTo(0, 3000);")
# time.sleep(1)

# driver.execute_script("window.scrollTo(0, 3500);")
# time.sleep(1)

# driver.execute_script("window.scrollTo(0, 4000);")
# time.sleep(1)

# driver.execute_script("window.scrollTo(0, 4500);")
# time.sleep(0.5)

# driver.execute_script("window.scrollTo(0, 5000);")
# time.sleep(0.5)

# driver.execute_script("window.scrollTo(0, 5500);")
# time.sleep(0.5)

# driver.execute_script("window.scrollTo(0, 6000);")
# time.sleep(0.5)

# driver.execute_script("window.scrollTo(0, 6500);")
# time.sleep(0.5)

# driver.execute_script("window.scrollTo(0, 7000);")
# time.sleep(2)

# IMDb_rating
rating = None
total_vote = None
number_of_stars = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
percent_and_number = []
percent_people_vote = []
number_people_vote = []

# get link
view_user_rating_element = driver.find_elements(By.CSS_SELECTOR, '*[aria-label="View User Ratings"]')

if view_user_rating_element:
    link_view_user_rating_element = view_user_rating_element[0].get_attribute("href")
    if link_view_user_rating_element:
        driver.get(link_view_user_rating_element)
        # time.sleep(1)

        wrapper_element = driver.find_elements(By.CSS_SELECTOR, '*[class="sc-5931bdee-0 jtILVy"]')

        # Rating
        rating_element = wrapper_element[0].find_elements(By.CSS_SELECTOR, '*[class="sc-5931bdee-1 jUnWeS"]')
        rating = rating_element[0].text
        rating += "/10"

        # Total vote
        total_vote_element = wrapper_element[0].find_elements(By.CSS_SELECTOR, 'div')
        total_vote = total_vote_element[1].text

        # percent and number
        for i in range(1, 11):
            element_command = 'chart-bar-1-labels-' + str(i - 1)
            command_element = driver.find_elements(By.ID, element_command)
            percent_and_number.append(command_element[0].text)

            parts = command_element[0].text.split()

            # percent_people_vote
            percent_people_vote.append(parts[0])

            # number_people_vote
            number_people_vote.append(parts[1].strip('()'))

print(rating)
print(total_vote)
print(number_of_stars)
print(percent_people_vote)
print(number_people_vote)

# # insert rating table -------------------------------------------------------
# insert_str = "INSERT INTO `filmdata`.`rating` (`rating_id`, `movie_id`, `number_of_stars`, `percent_people_vote`, `number_people_vote`) VALUES (%s, %s, %s, %s, %s)"
# # rating_id = 1

# for i in range(len(percent_people_vote)):
#     data = (rating_id, movie_id, number_of_stars[i], percent_people_vote[i], number_people_vote[i])
#     mycursor.execute(insert_str, data)
#     conn.commit()

#     rating_id += 1

mycursor.close()
driver.close()