# Kernael92's Instagram
# https://kernel-instagram.herokuapp.com/



## Built By [Kernael Apuko](https://github.com/kernael92/)

## Description
This is an application that allows authenticated users to create an instagram profile,upload pictures, view, like and comment on other users pictures as well as follow or unfollow other users. The admin is responsible for uploading, editing or deleting images and profiles.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* Sign in to the application to start using.
* Upload pictures into the application.
* See their profiles with all their pictures.
* Follow other users and see their pictures on their timelines
* Like a picture and leave a comment.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Create a profile and upload images.
* Delete images
* Update image post details.
* Comment and like images


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all profiles | **Home page** | Clickable links to view a users profile |
| Comment and like on a users uploaded photo| **On  click** | number of likes and comments on a photo|
| To upload an image  | **Through Admin dashboard** | Add the name and caption of the image|
| To edit profile | **Through Admin dashboard** | Redirected to the  profile settings and edit the profile picture as well as the bio|
| To delete a profile,comment,like or image  | **Through Admin dashboard** | click on any of the  objects and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by username of the user|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt
* Django authentication

### Cloning
* In your terminal:

        $ git clone https://github.com/kernael92/kernel-instagram
        $ cd kernel-instagram

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test images

## Technologies Used
* Python3.6
* Django and postgresql

## License

Copyright (c) 2018 Kernael92

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
