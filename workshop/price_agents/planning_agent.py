from typing import Optional, List
from price_agents.agent import Agent as BaseAgent
from price_agents.deals import Deal, Opportunity
from price_agents.scanner_agent import ScannerAgent
from price_agents.frontier_agent import FrontierAgent
from price_agents.specialist_agent import SpecialistAgent
from price_agents.messaging_agent import MessagingAgent


class PlanningAgent(BaseAgent):

    name = "Planning Agent"
    color = BaseAgent.GREEN
    DEAL_THRESHOLD = 50

    def __init__(self, collection):
        """
        Create instances of the 3 Agents that this planner coordinates across
        """
        self.log("Planning Agent is initializing")
        self.scanner = ScannerAgent()
        self.frontier = FrontierAgent(collection)
        self.specialist = SpecialistAgent()
        self.messenger = MessagingAgent()
        self.log("Planning Agent is ready")

    def run(self, deal: Deal) -> Opportunity:
        """
        Run the workflow for a particular deal
        :param deal: the deal, summarized from an RSS scrape
        :returns: an opportunity including the discount
        """
        self.log("Planning Agent is pricing up a potential deal")
        estimate1 = self.frontier.price(deal.product_description)
        estimate2 = self.specialist.price(deal.product_description)
        estimate = (estimate1 + estimate2) / 2.0
        discount = estimate - deal.price
        self.log(f"Planning Agent has processed a deal with discount ${discount:.2f}")
        return Opportunity(deal=deal, estimate=estimate, discount=discount)

    def plan(self, memory: List[Opportunity] = []) -> Optional[Opportunity]:
        """
        Run the full workflow:
        1. Use the ScannerAgent to find deals from RSS feeds
        2. Use the SpecialistAgent and FrontierAgent to estimate them
        3. Use the MessagingAgent to send a notification of deals
        We could have an LLM come up with this workflow, providing it with the Tools for each step
        But that would be overkill in this case as the workflow is simple and fixed; no intelligent triaging is required.
        :param memory: a list of Opportunities that have been surfaced in the past
        :return: an Opportunity if one was surfaced, otherwise None
        """
        self.log("Planning Agent is kicking off a run")
        selection = self.scanner.scan(memory=memory)
        if selection:
            opportunities = [self.run(deal) for deal in selection.deals[:5]]
            opportunities.sort(key=lambda opp: opp.discount, reverse=True)
            best = opportunities[0]
            self.log(f"Planning Agent has identified the best deal has discount ${best.discount:.2f}")
            if best.discount > self.DEAL_THRESHOLD:
                self.messenger.alert(best)
            self.log("Planning Agent has completed a run")
            return best if best.discount > self.DEAL_THRESHOLD else None
        return None
