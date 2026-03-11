using BulkyBookWeb.Data;
using BulkyBookWeb.Models;
using Microsoft.AspNetCore.Mvc;

namespace BulkyBookWeb.Controllers
{
    public class CategoryController : Controller
    {
        private readonly ApplicationDbContext _db;
        public CategoryController(ApplicationDbContext db)
        {
            _db = db;
        }

        //: Category/ Index
        public IActionResult Index()
        {
            List<Category> objCategoryList = _db.Catagories.ToList();
            return View(objCategoryList);
        }

        //: Category/ Create 
        public IActionResult create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Category obj)
        {
            if (obj.Name == obj.DisplayOrder.ToString())
            {
                ModelState.AddModelError("name", "The Display Order cannot exactly match the name.");
            }
            //if (obj.Name != null && obj.Name.ToLower() == "test")
            //{
            //    ModelState.AddModelError("", "Test is an invalid value");
            //}
            if (ModelState.IsValid)
            {
                _db.Catagories.Add(obj);
                _db.SaveChanges();
                TempData["success"] = "Category created succesfully";
                return RedirectToAction("Index", "Category");
            }
            return View(obj);
        }

        //: Category/ Edit
        public IActionResult Edit(int? CategoryID)
        {
            if (CategoryID == null || CategoryID == 0)
            {
                return NotFound();
            }
            Category? categoryFromDb = _db.Catagories.Find(CategoryID);
            if (categoryFromDb == null)
            {
                return NotFound();
            }
            return View(categoryFromDb);
        }

        [HttpPost]
        public IActionResult Edit(Category obj)
        {
            //if (obj.Name == obj.DisplayOrder.ToString())
            //{
            //    ModelState.AddModelError("name", "The Display Order cannot exactly match the name.");
            //}
            //if (obj.Name != null && obj.Name.ToLower() == "test")
            //{
            //    ModelState.AddModelError("", "Test is an invalid value");
            //}
            if (ModelState.IsValid)
            {
                _db.Catagories.Update(obj);
                _db.SaveChanges();
                TempData["success"] = "Category Updated succesfully";
                return RedirectToAction("Index", "Category");
            }
            return View(obj);
        }

        //: Category/ Delete
        public IActionResult Delete(int? CategoryID)
        {
            if (CategoryID == null || CategoryID == 0)
            {
                return NotFound();
            }
            Category? categoryFromDb = _db.Catagories.Find(CategoryID);
            if (categoryFromDb == null)
            {
                return NotFound();
            }
            return View(categoryFromDb);
        }

        [HttpPost, ActionName("Delete")]
        public IActionResult DeletePOST(int? CategoryID)//get the id that user want to delete
        {
            Category? obj = _db.Catagories.Find(CategoryID);
            if(obj == null)
            {
                return NotFound();
            }
            _db.Catagories.Remove(obj);
            _db.SaveChanges();
            TempData["success"] = "Category Deleted succesfully";
            return RedirectToAction("Index");
        }
    }
}