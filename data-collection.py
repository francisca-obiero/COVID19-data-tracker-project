# data-collection.py

try:
    import kagglehub
    print("Attempting to download dataset with kagglehub...")
    # Use the correct dataset slug from Kaggle
    path = kagglehub.dataset_download("caesarmario/our-world-in-data-covid19-dataset")
    print("Path to dataset files:", path)
except ImportError:
    print("kagglehub is not installed. Please install it with: pip install kagglehub")
except Exception as e:
    print("kagglehub download failed:", e)
    print("Attempting to download using Kaggle API instead...")

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        import os

        # Authenticate Kaggle API (requires kaggle.json in ~/.kaggle or environment variables)
        api = KaggleApi()
        api.authenticate()

        dataset = "caesarmario/our-world-in-data-covid19-dataset"
        dest_dir = "./data"
        os.makedirs(dest_dir, exist_ok=True)

        print(f"Downloading dataset '{dataset}' to '{dest_dir}' ...")
        api.dataset_download_files(dataset, path=dest_dir, unzip=True)
        print(f"Dataset downloaded and extracted to {dest_dir}")
    except ImportError:
        print("kaggle package is not installed. Please install it with: pip install kaggle")
    except Exception as e2:
        print("Kaggle API download failed:", e2)
        print("Please ensure you have Kaggle API credentials set up correctly.")



