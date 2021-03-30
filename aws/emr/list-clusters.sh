LIST_CLUSTERS=`
aws emr list-clusters \
    --region us-east-1 \
    --active \
    --output json \
    --query 'Clusters[*].[Id]' \
    --profile socialminer`

echo $LIST_CLUSTERS