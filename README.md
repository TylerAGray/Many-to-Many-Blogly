# Many-to-Many-Blogly
This includes Parts 1, 2, & 3.

## **Part Three: Add M2M Relationship**

The last part will be to add a “tagging” feature.

### **Tag Model**

![Screen Shot 2023-05-08 at 3.03.13 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4b764dd-ee1f-450a-a913-e14353e18216/Screen_Shot_2023-05-08_at_3.03.13_PM.png)

The site will have a table of tags — there should be an SQLAlchemy model for this:

- ***id***
- ***name***, (unique!)

There should also be a model for ***PostTag***, which joins together a ***Post*** and a ***Tag***. It will have foreign keys for the both the ***post_id*** and ***tag_id***. Since we don’t want the same post to be tagged to the same tag more than once, we’ll want the combination of post + tag to be unique. It also makes sense that neither the ***post_id*** nor ***tag_id*** can be null. Therefore, we’ll use a “composite primary key” for this table— a primary key made of more than one field. You may have to do some research to learn how to do this in SQLAlchemy.

Add relationships so you can see the ***.tags*** for a post, and the ***.posts*** for a tag.

**STOP** and play around with this feature in ***IPython*** before continuing.

### **User Interface**

1. **Add Tag**

![Screen Shot 2023-05-08 at 3.04.45 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/adcb908c-31bc-469e-934a-f7df80b75dd2/Screen_Shot_2023-05-08_at_3.04.45_PM.png)

1. **Edit Tag**

![Screen Shot 2023-05-08 at 3.09.35 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41092caa-0fb7-43ff-a794-1a2be68296cf/Screen_Shot_2023-05-08_at_3.09.35_PM.png)

1. **List Tag**

![Screen Shot 2023-05-08 at 3.11.42 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c61055c9-d050-415a-88f2-f5fdfb644dd5/Screen_Shot_2023-05-08_at_3.11.42_PM.png)

1. **Show Tag**

![Screen Shot 2023-05-08 at 3.14.48 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/527c480e-63a4-4d62-a97a-25f278ad4d3d/Screen_Shot_2023-05-08_at_3.14.48_PM.png)

1.  **Show Post With Tags**
    
    ![Screen Shot 2023-05-08 at 3.13.19 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e236b58b-1650-480d-98a7-9b276a634347/Screen_Shot_2023-05-08_at_3.13.19_PM.png)
    
2. **Add Post With Tags**

![Screen Shot 2023-05-08 at 3.16.01 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82c29a03-c0f8-4e9f-b985-749ab10a571d/Screen_Shot_2023-05-08_at_3.16.01_PM.png)

1. **Edit Post With Tags**

![Screen Shot 2023-05-08 at 3.17.48 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ed79536-7149-430c-85e8-ef1a220484da/Screen_Shot_2023-05-08_at_3.17.48_PM.png)

### **Add Routes**

**GET */tags :*** Lists all tags, with links to the tag detail page.

**GET */tags/[tag-id] :*** Show detail about a tag. Have links to edit form and to delete.

**GET */tags/new :*** Shows a form to add a new tag.

**POST */tags/new :*** Process add form, adds tag, and redirect to tag list.

**GET */tags/[tag-id]/edit :*** Show edit form for a tag.

**POST */tags/[tag-id]/edit :*** Process edit form, edit tag, and redirects to the tags list.

**POST */tags/[tag-id]/delete :*** Delete a tag.

### **Update Routes for Posts**

Update the route that shows a post so that it shows all the tags for that post.

Update the routes for adding/editing posts so that it shows a listing of the tags and lets you pick which tag(s) apply to that post. (You can use whatever form element you want here: a multi-select, a list of checkboxes, or any other way you can solve this.

<aside>
💡 **Hint:** The normal way to get a value from a form, `request.form['key']`, only returns *one* value from this form. To get all of the values for that key in the form, you’ll want to investigate ***.getlist**
