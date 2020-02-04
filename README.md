# Scripts to extract ECE1410 submissions

### Instructions

1. Download `submissions.zip` file
2. Download current `test.cpp` file
3. Run extract script

        python src/extract.py --submissions=path/to/submissions.zip --solutions=path/to/current/test.cpp --folder=name_of_folder_to_store_submissions --compile

    - Script will create an executable if everything compiles. If it doesn't compile, there will be an `error.txt` file.
        - To find all students code that didn't compile:

                cd directory/where/all/folders/are
                find . | grep error.txt
    - Script will create a `files.txt`. Lists all of the files students turned in
4. Check all code
    - In students each directory run `src/new_grade.py` script to create `grade.txt`. It will less all of the files turned in for inspection, then prompt for grade and comment.
        - Need to figure out how to upload the comment to canvas with the `.csv` file.
5. Download `.csv` file for current assignment from canvas with all the grades in it.
    - Right now all the grades will be blank
5. Create new `.csv` file
    - From the top directory, run `src/grade.py` and it will create a new `.csv` file to upload to canvas.
            
            python src/grade.py --path=path/to/all/submissions --csv=path/to/file.csv --column=Column where the grades will go
	
    - Example:

            python src/grade.py --path=hw2/submissions/ --csv=grads.csv --column=j

7. Upload `.csv` file to canvas
