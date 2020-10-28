FROM node

WORKDIR /urs/app

COPY ./package*.json ./

RUN npm install --only-production --no-optional

COPY . .

EXPOSE 3000

CMD npm start