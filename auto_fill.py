import os
from selenium import webdriver


submission_dir = 'images'

dir_list = list(os.listdir(submission_dir))


for directory in dir_list:
    file_list = list(os.listdir(os.path.join(submission_dir,directory)))
    if len(file_list) != 0:
        file_tup = (directory,file_list[0])
print(file_tup)

image_name = 'test60-NoCCANoAck-vazao-5-36'
num_nodes = 60

#Web

driver = webdriver.Chrome()

driver.get('http://twonet.cs.uh.edu/webentry/login.html')

#Login
id_box = driver.find_element_by_name('username')
pass_box = driver.find_element_by_name('password')
login_button = driver.find_element_by_class_name('button')

id_box.send_keys('nildo')
pass_box.send_keys('meneze')
login_button.click()

#Upload Imagem
driver.get('http://twonet.cs.uh.edu/webentry/image_page.php')

image_button = driver.find_element_by_name('upload')
image_button.click()

imagename_box = driver.find_element_by_name('imagename')
imagename_box.send_keys(image_name)

image_file = driver.find_element_by_name('file')
imagefile_location = os.path.join(submission_dir, file_tup[0],file_tup[1])
image_file.send_keys('/home/newuser/AutomatedExperiments/' + imagefile_location)

upload_button = driver.find_element_by_xpath("//form[@id='mainform']/table//tr[4]/td[2]/input[1]")
#upload_button.click()

#Create Configuration
driver.get('http://twonet.cs.uh.edu/webentry/configuration_page.php')

cfg_button = driver.find_element_by_name('new_cfg')
cfg_button.click()

cfgname_box = driver.find_element_by_name('cfg_name')
cfgname_box.send_keys(image_name)


select_image = driver.find_element_by_xpath("//select[@id='sel_left']/option[1]")
select_image.click()

selectimage_button = driver.find_element_by_xpath("//form[@id='mainform']/table[2]//tr[2]/td[2]/input[1]")
selectimage_button.click()

assign_motes_button = driver.find_element_by_name('assign_btn')
assign_motes_button.click()

#Assign Motes
select_image = driver.find_element_by_xpath("//select[@id='sel_image']/option[1]")
select_image.click()

selectnode_button = driver.find_element_by_xpath("//form[@id='mainform']/table[1]//tr[2]/td[4]/input[1]")

for i in range(num_nodes):
    select_node = driver.find_element_by_xpath("//select[@id='sel_left']/option[1]")
    select_node.click()
    selectnode_button.click()

submitcfg_button = driver.find_element_by_id('submit_btn')
#submitcfg_button.click()

#Send Task
driver.get('http://twonet.cs.uh.edu/webentry/task_page.php')

task_button = driver.find_element_by_name('new_task')
task_button.click()

task_box = driver.find_element_by_id('task_name')
task_box.send_keys(image_name)

time_slot = driver.find_element_by_css_selector('li.ui-widget-content.ui-selectee')
time_slot.click()

submit_button = driver.find_element_by_xpath("//form[@id='mainform']/table[1]//tr[3]/td[3]/input[1]")
submit_button.click()
