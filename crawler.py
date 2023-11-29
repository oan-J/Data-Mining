import random
import pandas as pd
import time
from selenium import webdriver
from tqdm import tqdm, trange
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])


def getData(url):
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    print(url)
    time.sleep(10)

    userNames = []  
    userAddress = []  
    timeList = []   
    comments = []   
    likeNums = []   


    for i in trange(1,30):

        try:
            driver.find_element(by=By.XPATH,
                                value='//*[@id="login-pannel"]/div[2]').click()
        except:
            try:
                t = random.uniform(1.5, 2) 
                sw = random.randint(150, 180) 
                time.sleep(t)  

                userName = driver.find_element(by=By.XPATH,
                                            value= f"//*[@id='root']//div[{i}]/div/div[2]/div[1]/div[2]/div[1]/div/a/span/span/span/span/span").text
                print("userName",userName)
                time_ = driver.find_element(by= By.XPATH,
                                            value= f"//*[@id='root']//div[{i}]/div/div[2]/div[1]/div[2]/div[1]/p").text
                print("time_",time_)
                comment = driver.find_element(by= By.XPATH,
                                              value= f"//*[@id='root']//div[{i}]/div/div[2]/div[1]/p/span/span/span/span/span/span").text
                print("comment",comment)
                likeNum = driver.find_element(by=By.XPATH,
                                              value= f"//*[@id='root']//div[{i}]/div/div[2]/div[1]/div/div/div/p/span").text
                print("likeNum",likeNum)


                driver.find_element(by=By.XPATH,
                                value= f"//*[@id='root']//div[{i}]/div/div[2]/div[1]/div[2]/div[1]/div/a/span/span/span/span/span").click()

                time.sleep(t)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(t)
                print("***")

                try:
                    ip_address = (driver.find_element(by=By.XPATH,
                                                     value="//*[@id='root']/div").text.split('：')[2]).split()[0]
                    print("ip_address",ip_address)
                except:
                    ip_address = ""
                    print("no ip_address")

                time.sleep(0.2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.execute_script(f"window.scrollBy(0, {sw})")

                userNames.append(userName)
                userAddress.append(ip_address)

                timeList.append(time_)
                comments.append(comment)
                likeNums.append(likeNum)
                print(f"第{i}条下载完成！！！")

            except:
                continue

    return userNames, userAddress,   timeList, comments, likeNums



if __name__ == "__main__":

    id = ""
    url = f"https://www.douyin.com/video/{id}"
    userNames, userAddress,   timeList, comments, likeNums = getData(url)

    data = pd.DataFrame({ "userName":userNames, "userAddress": userAddress, "date": timeList, "comments": comments, "likeNuns": likeNums})

    data.to_csv(f"./result_ID{id}.csv") 
    print("**********done***********")
    
