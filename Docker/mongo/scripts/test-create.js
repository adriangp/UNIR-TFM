// Se crea la base de datos y se conecta
//var db = connect('127.0.0.1:27017/local'),
//    allTest = null;
conn = new Mongo();
db = conn.getDB("local");
db = db.getSiblingDB("test")

// Se crea una colección y se añaden documentos
db.nombres.insert({'nombre' : 'Pepe'});
db.nombres.insert({'nombre' : 'Luis'});
db.nombres.insert({'nombre' : 'Manolo'});
db.nombres.insert({'nombre' : 'Maria'});



