FROM python:3-alpine
MAINTAINER Hank Preston <hank.preston@gmail.com>
EXPOSE 8080

# Install Pre-reqs
RUN mkdir /app
ADD ./requirements.txt /app
RUN pip install -r /app/requirements.txt

# Add Static Files
COPY ./static /app/static

# Add Templates
COPY ./templates /app/templates

# Add Code
COPY ./demo_portal.py /app

# Create bot directory and add code
WORKDIR /app

# Run Bot
CMD [ "python", "demo_portal.py" ]