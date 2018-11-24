# Django Static Server
Nesse repositorio tem um pequeno projeto para criar sites estaticos 

## Para instalar o projeto

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Para customizar as paginas e criar templates

Paginas personalizadas devem ser adicionadas em `/pages`

O template padrão inclui o boostrap 4, jquery, popper.js, fontawesome 5.5
mas para personalizar o template ou para criar novos componentes padroes como menus use 
```
/sitebuilder/templates
```

para dar o build no projeto rode:
```
python builder build 
```

para dar o build de uma pagina de o comando :
```
python builder build pagina1 pagina2
```





