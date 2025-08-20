import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Example data (replace with the dataset given in your GA)
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create heatmap
plt.figure(figsize=(6,6))  # Make square figure
sns.heatmap(data, annot=True, fmt="d", cmap="Blues")
plt.tight_layout()

# Save temp image
plt.savefig("temp_chart.png", dpi=100)
plt.close()

# Ensure EXACT 512x512
img = Image.open("temp_chart.png")
img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
img_resized.save("chart.png", "PNG", optimize=True)
