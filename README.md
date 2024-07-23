# clase15-2bim

### Proceso de instalación de VueJs

#### Pasos

#### Primer Parte
1. Ingresar a https://github.com/nvm-sh/nvm "Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions"

2. Ejecutar en consoloa
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
3. Actualizar el profile
```
source ~/.profile
```
4. Probar algunos comandos:
```
nvm ls-remote
```
5. Instalar la versión
```
nvm install v20.15.1
```
6. Usar la versión
```
nvm use v20.15.1
```
7. Verificar la versión
```
node -v
```
8. Instalar el framewok de JS, VueJs
```
npm install -g @vue/cli
```
9. Instalar el paquete para manejar las rutas
```
npm install vue-router@4
```
10. Instalar el paquete para usar servicios desde VueJs
```
npm install axios
```
#### Segunda Parte

1. Ingresar a la carpeta demo-proyecto
2. Ejecutar el comando
```
npm run serve
```
