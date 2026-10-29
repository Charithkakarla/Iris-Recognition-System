import os
import time
import tkinter as tk
from tkinter import filedialog

import cv2

from util import display_images, find_best_match, show_details


if __name__ == "__main__":
    dataset_folder = os.path.join("train", "eye")
    print("Please select an image from the dataset for matching:")
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(
        initialdir=dataset_folder,
        title="Select Query Iris Image",
        filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")),
    )

    query_image = None
    individual_id = None
    session_id = None

    if image_path:
        try:
            query_image = cv2.imread(image_path)
            filename = os.path.basename(image_path)
            filename_no_ext = os.path.splitext(filename)[0]
            parts = filename_no_ext.split("_")
            if len(parts) == 3:
                individual_id = parts[0]
                session_id = parts[1]
                print(f"Selected image: {filename}")
            else:
                print(
                    "Error: Invalid filename format. "
                    f"Expected 'XXX_S_Y.jpg', but got {filename}"
                )
                query_image = None
        except Exception as e:
            print(f"Error loading image or parsing filename: {e}")
            query_image = None
    else:
        print("No image selected. Exiting.")

    if query_image is not None:
        start_time = time.time()
        best_match_id, similarity = find_best_match(
            dataset_folder, query_image, image_path
        )
        end_time = time.time()
        execution_time = end_time - start_time
        query_images = [query_image]

        print("Displaying input image:")
        display_images(query_images)
        print("Best match found:")
        print(f"Individual ID: {best_match_id}")
        print(f"Similarity: {similarity}")
        print(f"Execution Time: {execution_time} seconds")
        print(
            "Displaying segmentation and normalization process details "
            "for the input image:"
        )
        show_details(query_image)

        if best_match_id is not None:
            print(f"Displaying all images of the matched individual {best_match_id}:")
            individual_images = []
            for filename in os.listdir(dataset_folder):
                if (
                    filename.startswith(best_match_id)
                    and filename.lower().endswith((".jpg", ".jpeg", ".png"))
                ):
                    filepath = os.path.join(dataset_folder, filename)
                    img = cv2.imread(filepath)
                    individual_images.append(img)
            display_images(individual_images)

    cv2.destroyAllWindows()
