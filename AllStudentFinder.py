from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from AllStudentFinder_xpath import get_XPATH


driver = webdriver.Firefox()
# driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://erp.bzte.ac.ir/Dashboard")

sleep(10)
driver.switch_to.frame(1)
# print("avaz shod")
elm = driver.find_element(By.XPATH,get_XPATH("dashbord", "vorodBeSamane"))
# print("ta inja omade")
elm.click()


driver.switch_to.default_content()
iframe = driver.find_element(By.ID,"iframe_4149")
driver.switch_to.frame(iframe)
print("kheir nabini")
username = driver.find_element(By.ID,get_XPATH("login_page","username"))
username.send_keys("4012114125")
print("username ja gozari shod ")
password = driver.find_element(By.ID,get_XPATH("login_page", "password"))
password.send_keys("0025577093")
print("password vared shod")
login = driver.find_element(By.XPATH,get_XPATH("login_page", "vorod"))
login.click()

sleep(2)
driver.switch_to.default_content()
elm = driver.find_element(By.XPATH,get_XPATH("user_panel", "tabligh"))
elm.click()
sleep(3)
# ta inja varede safhe asli shodim

# TODO : vorod be safhe gap ha
driver.switch_to.default_content()
driver.find_element(By.XPATH,get_XPATH("user_panel", "socialNetworkbuttom")).click()
sleep(3)

#TODO : vared shodan be list daneshjoian
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH,get_XPATH ("socialNetwork", "socialNetworkframe")))
sleep (4)
driver.find_element(By.XPATH,get_XPATH("socialNetwork", "students_group")).click()
sleep(4)
driver.find_element(By.XPATH,get_XPATH("socialNetwork", "hamburger_list")).click()
sleep(4)
driver.find_element(By.XPATH,get_XPATH("socialNetwork", "group_management")).click()
sleep(4)
elm = driver.find_element(By.XPATH,get_XPATH("socialNetwork", "scrollElement"))

for i in range(300):
    driver.execute_script("arguments[0].scrollTo(0, %s)" %(i * 1200) , elm)
    sleep(2)




# # TODO : gereftane etelaate daneshjo
# students = driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]')
# students_text = students.text


# # //*[@id="scroll"]

# driver.execute_script("arguments[0].scrollTo(0, 3000)", elm)
