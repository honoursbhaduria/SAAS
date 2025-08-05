## SaaS Foundations
Build the foundations for a Software as a Service business by leveraging Django, Tailwind, htmx, Neon Postgres, Redis, and using whitenoise for static file managment 

The goal of this project is to learn how to create a reusable foundation for building SaaS products. When release, this course will span multiple topics and give you a solid foundation into build your foundation on SAAS .



### Sample dotenv to dotnev

values include :

>> * DJANGO_DEBUG=1 
>> * DJANGO_SECRET_KEY=""
>> * DATABASE_URL=""
>> * EMAIL_HOST="smtp.gmail.com"
>> * EMAIL_PORT="587"
>> * EMAIL_USE_TLS=True
>> * EMAIL_USE_SSL=False
>> * EMAIL_HOST_USER=""
>> * EMAIL_HOST_PASSWORD=""
>> * ADMIN_USER_EMAIL=""
>> ### In future 
>> * STRIPE_SECRET_KEY=""


###   Clone the Project

```bash
mkdir -p ~/dev/saas
cd ~/dev/saas
git clone https://github.com/honoursbhaduria/SaaS-Foundations .

```



### macOS / Linux 

```bash
python3 --version  # Make sure it's 3.11 or higher
python3 -m venv venv
source venv/bin/activate

```

### Windows 


```bash
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate

```

### Install Requirements
>> With your virtual environment activated:


```bash
pip install --upgrade pip
pip install -r requirements.txt

```

###  Setup Environment Variables


```bash
cp .env.sample .env
cat .env

```

### Generate Django Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Paste the generated key into .env under DJANGO_SECRET_KEY.

### Run Migrations
```bash
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
cd src
python manage.py migrate
```
### Create Superuser

```bash
python manage.py createsuperuser

```

### Pull Vendor Static Files

```bash
python manage.py vendor_pull


```

### Setup Stripe Integration

Sign up at Stripe

Get your Secret API Key:

Dashboard > Developers > API keys > Secret key


### Update your .env file with:

```bash
STRIPE_SECRET_KEY="your_stripe_secret_key"
 ```

###  Run the Server

```bash
python manage.py runserver

 ```

In development — course and foundation are actively being built. Much more coming soon!

### Contribute

Want to help or learn by contributing? Open an issue or pull request!


