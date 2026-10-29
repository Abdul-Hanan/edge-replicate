import cv2
import numpy as np

def generate_synthetic_image(width=120, height=80):
    """
    Generates a small synthetic image with distinct color regions for testing.
    The image has a grey background with a red square, a blue square,
    a green circle, and a yellow line to clearly show edge replication.

    Args:
        width (int): Desired width of the synthetic image.
        height (int): Desired height of the synthetic image.

    Returns:
        numpy.ndarray: A BGR image (height x width x 3) of type np.uint8.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)

    # Background: Light Gray
    img[:, :] = [180, 180, 180] # BGR

    # Top-left square: Red
    sq1_size = min(width, height) // 3
    img[10:10+sq1_size, 10:10+sq1_size] = [0, 0, 255] # BGR

    # Bottom-right square: Blue
    sq2_size = min(width, height) // 4
    img[height-10-sq2_size:height-10, width-10-sq2_size:width-10] = [255, 0, 0] # BGR

    # Center circle: Green
    center_x, center_y = width // 2, height // 2
    radius = min(width, height) // 6
    cv2.circle(img, (center_x, center_y), radius, [0, 255, 0], -1) # BGR, -1 for filled

    # A diagonal line: Yellow
    cv2.line(img, (5, height - 5), (width - 5, 5), [0, 255, 255], 2) # BGR, thickness 2

    return img

def main():
    """
    Main function to generate an image, expand its canvas by replicating
    edge pixels, and save the original and expanded images.
    """
    print("Edge Replicate: Starting image processing...")

    # 1. Generate a synthetic input image
    # We use a relatively small image to clearly visualize the border expansion.
    original_image = generate_synthetic_image(width=120, height=80)
    print(f"Generated original image with shape: {original_image.shape}")

    # Define paths for output images
    original_output_path = "original_image.png"
    expanded_output_path = "expanded_image.png"

    # Save the original image for reference
    cv2.imwrite(original_output_path, original_image)
    print(f"Original image saved to {original_output_path}")

    # 2. Define the border size for expansion
    # This determines how many pixels the canvas will be extended on each side.
    border_size = 50 # Pixels to expand on the top, bottom, left, and right

    # 3. Create a larger canvas and copy the original image to the center,
    #    filling the surrounding border region by extending colors.
    #    cv2.BORDER_REPLICATE is used to achieve the desired effect:
    #    the nearest border pixels are replicated outwards to fill the new region.
    expanded_image = cv2.copyMakeBorder(
        original_image,
        border_size,      # Top border width
        border_size,      # Bottom border width
        border_size,      # Left border width
        border_size,      # Right border width
        cv2.BORDER_REPLICATE # Border type: replicate the edge pixels
    )
    print(f"Expanded image created with shape: {expanded_image.shape}")

    # 4. Save the expanded image to a file
    cv2.imwrite(expanded_output_path, expanded_image)
    print(f"Expanded image saved to {expanded_output_path}")

    print("Edge Replicate: Processing complete.")

if __name__ == "__main__":
    main()