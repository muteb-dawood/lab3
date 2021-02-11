#!/usr/bin/env python
# coding: utf-8

# In[1]:


def conform(fav):
    fav=42
    return fav


# In[2]:


if __name__=="__main__":
    print ('welcome!')
    fav=7
    conform(fav)
    print("my favorite # is", fav)


# In[4]:


student={'A':28,'B':25,'C':32,'D':25}
def test(student):
    new={'E':30,'F':28}
    student.update(new)
    print("inside the fuction",student)
    return
test(student)
print("outside the function:",student)


# In[6]:


class student:
    
    def __init__(self, name):
        self.name=name
        self.course_list= []
std=student("Muteb")
print(std.name)


# In[8]:


class student:
    
    def __init__(self, name):
        self.name=name
        self.course_list= []
    def add(self, new_course):
        self.course_list.append(new_course)
        
std=student("Muteb")
std.add("python")
print(std.course_list)


# In[11]:


class student:
    
    def __init__(self, name):
        self.name=name
        self.course_list= []
    def add(self, new_course):
        self.course_list.append(new_course)
        
std=student("Muteb")
txt = input("type somthing to test out: ")
std.add(txt)
print(std.course_list)


# In[12]:


class person:
    
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname= lname
        
    def printname(self):
        print(self.firstname, self.lastname)

class Professor(person):
    pass
mhd = Professor("muteb", "abdullah")
mhd.printname()


# In[ ]:




