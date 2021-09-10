Setting up

1) Go to "Main Part > Imports and Directory Information." In the second cell under this part is where you will change the condition Single/Dyadic/SingleC. For now, you can let it be in "Single", but you can change it to any of the other two if you prefer to run the preprocessing for the conditions in a different order, depending on run time (Single - 26 subs, Dyadic - 16 subs, SingleC - 10 subs).

2) Uncomment the line ```DATA_PATH = LAB_DATA_PATH```

3) Now run the two cells under "Imports and Directory Information"


Preprocessing

1) Navigate to the first cell under "Combine the eyetracking data." In the first few lines, you will see how I've converted the collider names from animate_collider_list.csv to lists for the hand/phone/avatar colliders. If you've made any changes to the animate_collider_list, especially if you've changed the value of any source_collider_name, you would have to make changes here accordingly. Hopefully this is self-explanatory.

2) Run this cell. This will run for all subjects in a given condition and will take the longest time.

3) Once this is complete (It will print progress of how many subjects are remaining), change the variable ```condition``` in the second cell under "Imports and Directory Information" (above) and run this (directory) cell again. Then run the preprocessing cell once more. Repeat until all conditions Single/Dyadic/SingleC have been processed.


Interpolation

1) Navigate to the first cell under "Interpolation of the data to minimize cut clustering (based on Walter, 2021)"

2) Run this cell for whichever the current condition is.

3) Once this is complete, repeat for the other conditions by changing the value of the variable of ```condition``` to Single/Dyadic/SingleC as necessary, same as above. 


Pushing

1) Push the ```[subID]_interpolation_df.csv``` files in "Results/Single", "Results/Dyadic", and "Results/SingleC" to GitHub. The ```_CompleteHitpoint.csv``` files are too big and should already be in the .gitignore file.


Good luck and thank you :^)