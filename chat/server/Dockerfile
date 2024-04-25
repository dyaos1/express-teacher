FROM node:21-slim
WORKDIR /server
COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 3001
CMD ["node", "app.js"]
