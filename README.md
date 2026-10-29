# edge-replicate

Expands an image canvas by replicating the nearest edge pixels outwards.

## How it works
This project loads a synthetic image, then creates a larger canvas. It copies the original image to the center of this new canvas and fills the surrounding border region by extending the colors of the nearest edge pixels from the original image outwards. This technique is often used in image processing to avoid abrupt edges when processing images near their boundaries.

The core logic is implemented efficiently using OpenCV's `cv2.copyMakeBorder` function with the `cv2.BORDER_REPLICATE` type.

## How to run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/edge-replicate.git
    cd edge-replicate
    ```
    (Note: Replace `https://github.com/your-username/edge-replicate.git` with the actual repo URL if this were a real project.)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the script:**
    ```bash
    python main.py
    ```

## Output
Upon successful execution, the script will generate two image files in the same directory:
-   `original_image.png`: The small, synthetically generated input image.
-   `expanded_image.png`: The larger image with the original image centered and its borders filled by replicating edge pixels.