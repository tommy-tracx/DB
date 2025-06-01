FROM node:20-slim as build
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install --production=false
COPY src ./src
RUN npx vite build --outDir /dist

FROM nginx:alpine
COPY --from=build /dist /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]
