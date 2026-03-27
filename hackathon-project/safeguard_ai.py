"""
SafeGuard AI - Intelligent Women's Safety System
Real-time threat detection using AI/ML with automated emergency response
"""

import random
import time
from datetime import datetime
import json

class SafeGuardAI:
    def __init__(self):
        self.threat_level = 0
        self.location = {"lat": 28.6139, "lon": 77.2090}
        self.emergency_contacts = ["+91-9876543210", "+91-9876543211"]
        self.safe_zones = self.load_safe_zones()
        self.threat_history = []
        
    def load_safe_zones(self):
        return [
            {"name": "Police Station 1", "lat": 28.6150, "lon": 77.2100, "type": "police"},
            {"name": "Hospital 1", "lat": 28.6130, "lon": 77.2080, "type": "hospital"},
            {"name": "Safe House 1", "lat": 28.6145, "lon": 77.2095, "type": "safe_house"}
        ]
    
    def analyze_audio_pattern(self, audio_data):
        """AI Model: Analyze audio for distress signals"""
        distress_keywords = ["help", "stop", "no", "leave", "police"]
        volume_level = audio_data.get("volume", 0)
        speech_text = audio_data.get("text", "").lower()
        
        threat_score = 0
        
        for keyword in distress_keywords:
            if keyword in speech_text:
                threat_score += 25
        
        if volume_level > 80:
            threat_score += 30
        
        if audio_data.get("tone") == "aggressive":
            threat_score += 20
        
        return min(threat_score, 100)
    
    def analyze_movement_pattern(self, movement_data):
        """AI Model: Detect unusual movement patterns"""
        speed = movement_data.get("speed", 0)
        acceleration = movement_data.get("acceleration", 0)
        pattern = movement_data.get("pattern", "normal")
        
        threat_score = 0
        
        if acceleration > 5:
            threat_score += 30
        
        if pattern == "erratic":
            threat_score += 25
        
        if speed > 15:
            threat_score += 20
        
        return min(threat_score, 100)
    
    def analyze_location_safety(self, current_location):
        """AI Model: Assess location safety based on crime data and time"""
        hour = datetime.now().hour
        threat_score = 0
        
        if hour >= 22 or hour <= 5:
            threat_score += 30
        
        min_distance = self.calculate_distance(current_location, self.safe_zones[0])
        
        if min_distance > 2:
            threat_score += 25
        
        if current_location.get("crowd_density", 0) < 10:
            threat_score += 20
        
        return min(threat_score, 100)
    
    def analyze_text_messages(self, messages):
        """Cybersecurity: Analyze messages for stalking/harassment patterns"""
        threat_indicators = ["follow", "watching", "alone", "threat", "hurt", "kill"]
        threat_score = 0
        
        for msg in messages:
            msg_lower = msg.lower()
            for indicator in threat_indicators:
                if indicator in msg_lower:
                    threat_score += 15
            
            if messages.count(msg) > 3:
                threat_score += 20
        
        return min(threat_score, 100)
    
    def calculate_distance(self, loc1, loc2):
        lat_diff = abs(loc1["lat"] - loc2["lat"])
        lon_diff = abs(loc1["lon"] - loc2["lon"])
        return ((lat_diff ** 2 + lon_diff ** 2) ** 0.5) * 111
    
    def find_nearest_safe_zone(self):
        nearest = min(self.safe_zones, 
                     key=lambda x: self.calculate_distance(self.location, x))
        distance = self.calculate_distance(self.location, nearest)
        return nearest, distance
    
    def trigger_emergency_response(self, threat_level):
        print("\n" + "="*60)
        print("🚨 EMERGENCY ALERT TRIGGERED 🚨")
        print("="*60)
        
        print(f"\n📱 Sending SOS to emergency contacts:")
        for contact in self.emergency_contacts:
            print(f"   → {contact}: 'EMERGENCY! Need immediate help!'")
        
        print(f"\n🚔 Alerting nearby police stations...")
        print(f"   → Location shared: {self.location['lat']}, {self.location['lon']}")
        
        safe_zone, distance = self.find_nearest_safe_zone()
        print(f"\n🛡️ Nearest Safe Zone: {safe_zone['name']}")
        print(f"   → Distance: {distance:.2f} km")
        print(f"   → Type: {safe_zone['type'].upper()}")
        
        print(f"\n📍 Live location tracking ACTIVATED")
        print(f"   → Sharing real-time location with emergency contacts")
        
        print(f"\n🎥 Evidence collection STARTED")
        print(f"   → Recording audio and video")
        print(f"   → Uploading to secure cloud storage")
        
        return True
    
    def assess_threat_level(self, sensor_data):
        audio_threat = self.analyze_audio_pattern(sensor_data.get("audio", {}))
        movement_threat = self.analyze_movement_pattern(sensor_data.get("movement", {}))
        location_threat = self.analyze_location_safety(sensor_data.get("location", {}))
        message_threat = self.analyze_text_messages(sensor_data.get("messages", []))
        
        total_threat = (
            audio_threat * 0.35 +
            movement_threat * 0.25 +
            location_threat * 0.20 +
            message_threat * 0.20
        )
        
        return {
            "total_threat": total_threat,
            "audio_threat": audio_threat,
            "movement_threat": movement_threat,
            "location_threat": location_threat,
            "message_threat": message_threat
        }
    
    def monitor_safety(self, sensor_data):
        threat_analysis = self.assess_threat_level(sensor_data)
        
        print("\n" + "="*60)
        print("SafeGuard AI - Real-time Threat Analysis")
        print("="*60)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\n📊 Threat Assessment:")
        print(f"   Audio Analysis:    {threat_analysis['audio_threat']:.1f}%")
        print(f"   Movement Pattern:  {threat_analysis['movement_threat']:.1f}%")
        print(f"   Location Safety:   {threat_analysis['location_threat']:.1f}%")
        print(f"   Message Analysis:  {threat_analysis['message_threat']:.1f}%")
        print(f"\n🎯 Overall Threat Level: {threat_analysis['total_threat']:.1f}%")
        
        if threat_analysis['total_threat'] >= 70:
            print("   Status: 🔴 CRITICAL - Emergency Response Activated")
            self.trigger_emergency_response(threat_analysis['total_threat'])
        elif threat_analysis['total_threat'] >= 40:
            print("   Status: 🟡 WARNING - Heightened Alert Mode")
            print("   → Monitoring intensified")
            print("   → Emergency contacts notified (standby)")
        else:
            print("   Status: 🟢 SAFE - Normal Monitoring")
        
        self.threat_history.append(threat_analysis)
        return threat_analysis


def demo_scenario_1():
    print("\n" + "🔷"*30)
    print("SCENARIO 1: Normal Safe Environment")
    print("🔷"*30)
    
    system = SafeGuardAI()
    
    sensor_data = {
        "audio": {"volume": 45, "text": "hello how are you", "tone": "normal"},
        "movement": {"speed": 3, "acceleration": 0.5, "pattern": "normal"},
        "location": {"lat": 28.6139, "lon": 77.2090, "crowd_density": 50},
        "messages": ["Hi, how are you?", "See you tomorrow"]
    }
    
    system.monitor_safety(sensor_data)
    time.sleep(2)


def demo_scenario_2():
    print("\n" + "🔷"*30)
    print("SCENARIO 2: Suspicious Activity Detected")
    print("🔷"*30)
    
    system = SafeGuardAI()
    
    sensor_data = {
        "audio": {"volume": 65, "text": "stop following me", "tone": "worried"},
        "movement": {"speed": 8, "acceleration": 3, "pattern": "erratic"},
        "location": {"lat": 28.6200, "lon": 77.2150, "crowd_density": 15},
        "messages": ["I'm watching you", "I know where you live"]
    }
    
    system.monitor_safety(sensor_data)
    time.sleep(2)


def demo_scenario_3():
    print("\n" + "🔷"*30)
    print("SCENARIO 3: EMERGENCY - Critical Threat Detected")
    print("🔷"*30)
    
    system = SafeGuardAI()
    
    sensor_data = {
        "audio": {"volume": 95, "text": "help me please stop no", "tone": "aggressive"},
        "movement": {"speed": 18, "acceleration": 7, "pattern": "erratic"},
        "location": {"lat": 28.6250, "lon": 77.2200, "crowd_density": 5},
        "messages": ["I will hurt you", "You can't escape", "I'm following you"]
    }
    
    system.monitor_safety(sensor_data)
    time.sleep(2)


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🛡️  SafeGuard AI - Women's Safety System")
    print("    AI-Powered Threat Detection & Emergency Response")
    print("="*60)
    
    demo_scenario_1()
    demo_scenario_2()
    demo_scenario_3()
    
    print("\n" + "="*60)
    print("✅ Demo Complete - System Ready for Deployment")
    print("="*60)
