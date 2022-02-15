# Variables
variable "deployments_subdomains" {
  type        = list(string)
  description = "List of subdomains to be routed to Kubernetes Services."
}

# Subdomains required by Kubernetes Deployments
resource "aws_route53_record" "deployments_subdomains" {
  for_each = toset(var.deployments_subdomains)

  zone_id = data.aws_route53_zone.base_domain.id
  name    = "${each.key}.${aws_route53_record.eks_domain.fqdn}"
  type    = "CNAME"
  ttl     = "5"
  records = ["${data.kubernetes_service.ingress_gateway.load_balancer_ingress.0.hostname}"]
}
