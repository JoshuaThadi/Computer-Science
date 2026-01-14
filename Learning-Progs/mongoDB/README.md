## Lesson 1

A collection of data is called as document. A document is a field value pairs to represent the object.

A collection is a group of one or more documents.

A database is a group of one or more collection

documents → collection → database 

---

### 1.Database

open mongosh terminal and type mongosh to enable the connection.
**→ show dbs**

to see the list of all the databases.
**→ use <dbs_name>**
to switch in database.

we can create a database using “use”.
**→ use school**

to add a collection to the school database using method db.createCollection() and passing an argument like “students”.
**→ db.createCollection(”students”)**

to drop a current database we use method db.dropDatabase() without any argument.
**→db.dropDatabase()**

---

### 2.Insert

to insert a document or a input fields in students collection.
**→ db.students.insertOne({name:"spongebob", age:30, gpa:3.2})**

to return all documents with a collection.
**→ db.students.find()**

to insert many document in the collection with in an array.
**→ db.students.insertMany([{name:"Patrick", age:38, gpa:1.5},**
                          **{name:"Sandy", age:27, gpa:4.0},**
                          **{name:"Gary", age:18, gpa:2.5}])**

---

### 3.DataTypes

to insert all the data field in on command.
**→ db.students.insertOne({name:"Larry", age:32, gpa:3.4, fullTime: false //boolean,** 
                       **registerDate: new Date(), graduationDate: null,** 
                       **courses: ["Biology", "Chemistry", "Calculus"],  //array** 
                       **address: {street:"Queens Park", city:"Bikini Bottom", zip: 122110}})**

---

### 4.Delete

To remove a single document that matches a condition:
**→ db.students.deleteOne({ name: "Patrick" });**
This will delete the first document where `name` is `"Patrick"`.


To remove all documents that match a condition:
**→ db.students.deleteMany({ age: { $gt: 20 } });**

To remove all documents from the collection:
**→ db.students.deleteMany({});**

To delete a specific document by its `_id` in **MongoDB (`mongosh`)**, use the following command:
**→ db.students.deleteOne({ _id: ObjectId("67ee5fbe5de171f3814d7942") });**

---

### 5.Sorting and Limiting

to sort all the documents in ascending order.
**→ db.students.find().sort({name:1})**

to sort all the documents in decending order:
**→ db.students.find().sort({name:-1})**

to return the documents according to the limit: limit(1) will provide one documents, etc.
**→ db.students.find().limit(1)**

integration of limit and sort:
**→ school> db.students.find().sort({gpa:1}).limit(1)**

---

### 6.Find()

to find a particular document through the data field.
**→ db.students.find({gpa:3.2, fullTime:true})**

additional commands:

**→ db.students.find({}, {name:true})**
**→ school> db.students.find({}, {_id:false, name:true})**

---

### 7.Update()

to update a document using set.
**→ db.students.updateOne({name:"spongebob"}, {$set:{fullTime:true}})**


unset method to retrieve the update.
→ **db.students.updateOne({name:"spongebob"}, {$unset:{fullTime:true}})**


to update every document fullTime data field:
→ **db.students.updateMany({}, {$set:{fullTime:true}})**


to update fullTime to any document that does not contains fullTime data field
**→ db.students.updateMany({fullTime:{$exists:false}}, {$set:{fullTime:true}})**

---

### 8.Comparison Operators
1. not equal comparison operator
**→ db.students.find({name:{$ne:"spongebob"}})**

2. less than operator and less than equal to operator.
**→ db.students.find({age:{$lt:20}})**
**→ db.students.find({age:{$lte:20}})**

3. greater than operator and greater than equal to operator.
**→ db.students.find({age:{$gt:20}}**
**→ db.students.find({age:{$gte:20}}**

4. using greater and less than operator togther
**→ db.students.find({gpa: {$gte:3, $lte:4}})**

5. ‘in’ operator which executes the documents in the collection and ‘nin’ which means ‘not in’ which will execute the documents that are not in the command.
**→ db.students.find({name:{$in:["spongebob", "Patrick", "Sandy"]}})**
**→** **db.students.find({name:{$nin:["spongebob", "Patrick", "Sandy"]}})**

---

### 9.Logical Operators

Logical operators return data based on expression that evaluates to true or false
$and, $not, $nor, $or

1.And operator.
**→ db.students.find({$and: [{fullTime:false}, {age:{$lte:22}}]})**

2.Not operator.
**→ db.students.find({age:{$not:{$gte:30}}})**

3.Nor operator.
**→ db.students.find({$nor: [{fullTime:false}, {age:{$lte:22}}]})**

4.Or operator.
**→ db.students.find({$or: [{fullTime:false}, {age:{$lte:22}}]})**

---

### 10.Indexes and collections

MongoDB can use the index to limit the number of documents it must inspect.
**→ db.students.find({name:"Larry"}).explain("executionStats")**

to create an index.
**→ db.students.createIndex({name: 1})**

to fetch the index.
**→ db.students.getIndexes()**

to drop the index.
**→ db.students.dropIndex("name_1")**

Collections is a group of documents.
**→ show collections**

to create a collection.
**→ db.createCollection("teachers")**
**→ db.createCollection("teachers", {capped:true, size:10000000, max:100}, {autoIndexId:false})**

to drop a collection.
**→ db.teachers.drop()**