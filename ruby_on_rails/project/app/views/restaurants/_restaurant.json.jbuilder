json.extract! restaurant, :id, :name, :score, :description, :created_at, :updated_at
json.url restaurant_url(restaurant, format: :json)
