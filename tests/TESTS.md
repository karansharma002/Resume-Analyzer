### **1️⃣ Resume Text Extraction (PDF/DOCX)**  
✅ **Test Case 1:** Upload a valid PDF file  
- **Input:** Resume in PDF format  
- **Expected Output:** Extracted text displayed correctly  

✅ **Test Case 2:** Upload a valid DOCX file  
- **Input:** Resume in DOCX format  
- **Expected Output:** Extracted text displayed correctly  

✅ **Test Case 3:** Upload an unsupported file format (e.g., PNG, JPG)  
- **Input:** Image file  
- **Expected Output:** Error message: "Invalid file format"  

✅ **Test Case 4:** Upload a corrupt/empty PDF file  
- **Input:** Corrupt/empty file  
- **Expected Output:** Error message: "Unable to extract text"  

---

### **2️⃣ Resume Scoring System**  
✅ **Test Case 5:** Upload a well-formatted resume with relevant skills  
- **Input:** Resume containing job-specific keywords, experience, and skills  
- **Expected Output:** High resume score (e.g., 85% or above)  

✅ **Test Case 6:** Upload a resume with no relevant skills or experience  
- **Input:** Resume lacking required job skills  
- **Expected Output:** Low resume score with improvement suggestions  

✅ **Test Case 7:** Upload an incomplete resume (missing experience, education, etc.)  
- **Input:** Resume missing important sections  
- **Expected Output:** Error message: "Resume is incomplete"  

---

### **3️⃣ ATS Compatibility Check**  
✅ **Test Case 8:** Upload a resume with proper formatting (no tables, simple fonts)  
- **Input:** Well-structured ATS-friendly resume  
- **Expected Output:** High ATS score  

✅ **Test Case 9:** Upload a resume with images, columns, or fancy fonts  
- **Input:** Resume with non-ATS-friendly elements  
- **Expected Output:** Low ATS score with recommendations  

✅ **Test Case 10:** Upload a resume in an image format (JPG, PNG)  
- **Input:** Image-based resume  
- **Expected Output:** Error message: "Resume format not supported"  

---

### **4️⃣ AI-Based Suggestions & Recommendations**  
✅ **Test Case 11:** Upload a resume with missing action verbs  
- **Input:** Resume lacking strong action words (e.g., "worked on" instead of "developed")  
- **Expected Output:** AI suggests improvements with stronger phrasing  

✅ **Test Case 12:** Upload a resume without a summary section  
- **Input:** Resume missing a personal summary  
- **Expected Output:** AI suggests adding a summary for better impact  

✅ **Test Case 13:** Upload a resume with too much jargon  
- **Input:** Resume with overly complex language  
- **Expected Output:** AI suggests making it simpler and clearer  

---

### **5️⃣ Grammar & Formatting Checks**  
✅ **Test Case 14:** Upload a resume with grammatical errors  
- **Input:** Resume with typos and incorrect grammar  
- **Expected Output:** AI highlights errors and suggests corrections  

✅ **Test Case 15:** Upload a resume with inconsistent formatting (extra spaces, mixed fonts)  
- **Input:** Resume with mixed font styles and improper spacing  
- **Expected Output:** AI suggests standardizing the format  

✅ **Test Case 16:** Upload a resume with spelling mistakes  
- **Input:** Resume containing spelling errors  
- **Expected Output:** AI provides spelling corrections  

---

### **6️⃣ Performance & Edge Cases**  
✅ **Test Case 17:** Upload a large resume file (5MB+)  
- **Input:** Large-sized resume  
- **Expected Output:** System handles it without crashing  

✅ **Test Case 18:** Upload a resume with non-English text  
- **Input:** Resume written in another language  
- **Expected Output:** System should detect language or provide a warning  

✅ **Test Case 19:** Upload a resume with only an image watermark  
- **Input:** Resume with company logos/watermarks  
- **Expected Output:** Should not affect the text extraction  

✅ **Test Case 20:** Upload multiple resumes at once  
- **Input:** Multiple resume files uploaded  
- **Expected Output:** Error message: "Only one resume can be processed at a time"  

