# ESTsoft-BE-bootcamp-project-2-django

## Subject: Building a Singapore Travel Cafe with Django

### Objective
- Implement CRUD operations and user authentication using Django
- Deploy the backend server using AWS, Uwsgi, and Nginx


### Development Environment
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)

- Key library versions:
```
- asgiref==3.7.2
- Django==4.2.3
- sqlparse==0.4.4
- typing_extensions==4.7.1
```
### Deployment
  ![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white)
  ![Uswgi](https://img.shields.io/badge/uwsgi-488A99?style=for-the-badge&logo=uwsgi&logoColor=white)
  ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
  
### Development Timeline
- 2023.07.17 ~ 2023.07.20

### Deployment URL
- http://15.165.212.195/

### ERD Planning
![ERD](./architecture/django-project1.png)
- Initial planning did not include reply functionality. This was added later and not reflected in the ERD.

### Feature Planning (Mindmap)
![기능](./architecture/service%20mindmap.png)
 

### Page Implementation
#### Main Page
<img width="1440" alt="image" src="https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/00a78dbe-ae30-4f75-8820-7a640d043830">

#### Sign-up
![register](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/71a9cd48-28cb-42f1-8c11-07e0d5112ae9)

#### Login & Logout
![login_out](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/de44e27d-a913-4f6c-9e05-dc22bc313ae7)

#### Post List
<img width="1440" alt="image" src="https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/f115f4cc-c1e4-4791-be57-961bf60e3507">

#### Create Post
![post_write](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/392e766a-f651-45fc-84a1-1c1b696654c6)

#### Post Details (Notable Issue: Unable to delete hashtags)
![post_detail](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/93fdc42a-5e32-4512-9d23-57943000758a)

#### Post Search: Implemented hashtag table for search functionality
![search](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/26d0a2d2-ca77-4cc1-87a0-4927feaa0ce6)

#### Edit Post
![post_edit](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/d3d735ae-1426-4b73-9e55-d0312a7e7e42)

#### Delete Post (Redirects to list after deletion)
![delete_post](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/2ce07e12-111f-49cd-8727-23caf47577eb)

#### Commenting System: Create and delete comments
![comments](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/5ec4b198-8176-4a67-b3b5-679b44df86bb)

#### Reply System: Create and delete replies
![reply](https://github.com/sunse-kwon/ESTsoft-BE-bootcamp-project-2-django/assets/94329884/886d12d7-48ff-44cb-acbe-071bf3b85218)

### Challenges and Solutions
1. Deployment Issues: The application ran smoothly on localhost but encountered issues during deployment. Resolved by:

 - Opening TCP ports on AWS
  ![포트](./README-IMG/image.png)
 - Adding allowed hosts in settings.py
  ![allowed host](./README-IMG/image99.png)
- Configuring Uwsgi and Nginx with the help of online resources, despite initial difficulties
  
2. Reply Functionality: Initially failed to implement a recursive comment model for replies. Resolved by creating a separate Reply model and linking it via foreign key.


### Conclusion
This project marked my first experience with Django and deploying a server on AWS. It was a significant learning opportunity, providing a solid foundation for future development endeavors.

