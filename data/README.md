# Data Directory

## Structure

```
data/
├── raw/          # Original, unmodified source data
├── processed/    # Cleaned and transformed datasets ready for analysis
└── README.md     # This file
```

## Dataset Candidates

### DoorDash

| Dataset | Source | Description | Format | Size |
|---|---|---|---|---|
| Food Delivery across Canada (DoorDash) | [Kaggle](https://www.kaggle.com/datasets/satoshiss/food-delivery-in-canada-door-dash) | Restaurants with <30 min delivery in downtown Canadian cities, scraped from DoorDash | ZIP/CSV | ~197 KB |

### Deliveroo

| Dataset | Source | Description | Format | Size |
|---|---|---|---|---|
| Deliveroo Restaurant Dataset | [Kaggle](https://www.kaggle.com/datasets/polartech/deliveroo-restaurant-dataset) | Restaurants scraped from Deliveroo by zipcode — includes delivery fee, time, distance, rating, category | ZIP/CSV | ~1.7 MB |

### General Food Delivery

| Dataset | Source | Description | Format | Size |
|---|---|---|---|---|
| Food Delivery Dataset | [Kaggle](https://www.kaggle.com/datasets/gauravmalik26/food-delivery-dataset) | Delivery time estimation dataset, Asia-focused | ZIP/CSV | ~2 MB |
| Food Delivery Order History | [Kaggle](https://www.kaggle.com/datasets/sujalsuthar/food-delivery-order-history-data) | Order history data | CSV | — |

## Recommended Starting Point

**Deliveroo Restaurant Dataset** is the most analytically rich of the free options. It includes:
- `loc_name`, `description`, `delivery_fee`, `delivery_time`, `distance`
- `review_count`, `review_rating`
- `searched_category` (food category)
- `searched_zipcode`, `searched_lat`, `searched_lng`

Good for: funnel analysis by category, delivery fee vs. rating segmentation, geographic clustering.

## Download Instructions

All datasets require a free Kaggle account. Use the Kaggle CLI:

```bash
# Install Kaggle CLI
pip install kaggle

# Download Deliveroo dataset
kaggle datasets download -d polartech/deliveroo-restaurant-dataset -p data/raw/

# Download DoorDash Canada dataset
kaggle datasets download -d satoshiss/food-delivery-in-canada-door-dash -p data/raw/

# Unzip
unzip data/raw/deliveroo-restaurant-dataset.zip -d data/raw/deliveroo/
unzip data/raw/food-delivery-in-canada-door-dash.zip -d data/raw/doordash-canada/
```
