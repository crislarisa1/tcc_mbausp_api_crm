SELECT *
FROM `projeto-blz-portugal.dataset_ecommerce.checkouts_raw`
WHERE checkout_completed = FALSE
AND TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, HOUR) >= 1
AND marketing_consent = TRUE
