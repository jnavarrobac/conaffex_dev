const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();

app.use(express.static(path.join(__dirname, '/front_end')));
 
router.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/front_end/views/index.html'));
  // direccionamiento a la pagina inicial.
});
 
// 1 - Redireccionamos a las páginas de control de colaborador
router.get('/addcol',function(req,res){
  res.sendFile(path.join(__dirname+'/front_end/views/añadir_colaborador.html'));
});

router.get('/modcol',function(req,res){
    res.sendFile(path.join(__dirname+'/front_end/views/modificar_colaborador.html'));
  });
 

 
//add the router
app.use('/', router);
app.listen(process.env.port || 3000);
 
console.log('Running at Port 3000');   