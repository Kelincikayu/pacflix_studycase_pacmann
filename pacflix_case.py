#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install tabulate')


# In[2]:


from tabulate import tabulate


# In[4]:


tables = [
    ["Streamable", "Yes", "Yes", "Yes"],
    ["Downloadable", "Yes", "Yes", "Yes"],
    ["SD Quality", "Yes", "Yes", "Yes"],
    ["HD Quality", "No", "Yes", "Yes"],
    ["UHD Quality", "No", "No", "Yes"],
    ["Number of Device Allowed", 1, 2, 4],
    ["Price", 120000, 160000, 200000]
]


# In[5]:


headers = ["Services","Silver Plan", "Gold Plan", "Platinum Plan"]
print(tabulate(tables, headers))


# In[6]:


class Username:

  def __init__(self, name, period, ref_code, plan):
    self.name = name
    self.period = period
    self.ref_code = ref_code
    self.plan = plan
    self.prices = {"Silver Plan": 120_000, "Gold Plan": 160_000, "Platinum Plan":200_000}
    self.ref_disc = 0.04
    self.upgrade_disc = 0.05

  def upgrade_plan(self, new_plan): 
    plans = ["Silver Plan", "Gold Plan", "Platinum Plan"]
    prices = {"Silver Plan": 120_000, "Gold Plan": 160_000, "Platinum Plan":200_000}
    if plans.index(new_plan) > plans.index(self.plan):
      self.plan = new_plan
      price = prices[new_plan]
      if self.period > 12:
        upgrade_disc = 0.05
        discounted_price = price - price*upgrade_disc
        print(f'Plan upgrade to {new_plan}, with 5% discount. You only have to pay Rp.{discounted_price}')
      else:
        print(f'Plan upgrade to {new_plan}, your new billing will be at normal price Rp. {price}')
    else:
      print(f'Cannot Downgrade Plan')


  def new_user_discount(self, ref_code):
    period = self.period
    name = self.name
    valid_ref_code =["BR001A","IB001Z","BA001Q"] 
    if  ref_code in valid_ref_code and period == 1:
      print(f"Congratulation, {name}, the referal code is valid, you get discount for your first month payment")
      return self.ref_disc
    else:
      print("Ref_code is not valid or no longer valid")
      return 0

  def check_benefit(self):
    print("Username:", self.name)
    print("Period of subscription:", self.period, "month")
    print("Refferal code:", self.ref_code)
    print("Plan:", self.plan)

  def bill_this_month(self):
    price = self.prices[self.plan]
    ref_disc = self.new_user_discount(self.ref_code)
    if self.period == 1:
      price =price - price*ref_disc
    print(f"Your billing for this month is Rp. {price}")
    return price


# In[7]:


username1 = Username("Bradley", 15, "BR001A", "Platinum Plan")
username2 = Username("Ibel", 20, "IB001Z", "Silver Plan")
username3 = Username("Balqis", 10, "BA001Q", "Gold Plan")
username_new = Username("Bontop", 1, "BA001Q", "Gold Plan")


# In[8]:


username1.check_benefit()


# In[9]:


username1.bill_this_month()


# In[10]:


username2.check_benefit()
username2.bill_this_month()


# In[11]:


username3.check_benefit()
username3.bill_this_month()


# In[12]:


username_new.check_benefit()
username_new.bill_this_month()


# In[13]:


username3.upgrade_plan("Platinum Plan")


# In[14]:


username2.upgrade_plan("Gold Plan")


# In[15]:


username1.upgrade_plan("Gold Plan")


# In[ ]:




